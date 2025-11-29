import React, { useState } from "react";
import { sendMessage } from "./api";

function Chat() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    const res = await sendMessage(msg);
    setChat([...chat, { user: msg }, { bot: res.reply }]);
    setMsg("");
  };

  return (
    <div>
      <div className="chatbox">
        {chat.map((c, i) => (
          <p key={i}>
            {c.user && <b>You:</b>} {c.user}
            {c.bot && <b>MediMind:</b>} {c.bot}
          </p>
        ))}
      </div>

      <input
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Chat;
