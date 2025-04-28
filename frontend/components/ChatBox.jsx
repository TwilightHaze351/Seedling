import React, { useState } from 'react';

function ChatBox() {
    const [message, setMessage] = useState("");

    const handleSend = () => {
        console.log("Send:", message);
        setMessage("");
    };

    return (
        <div className="mt-4">
            <input value={message} onChange={e => setMessage(e.target.value)} className="border p-2" />
            <button onClick={handleSend} className="ml-2 p-2 bg-blue-500 text-white">Send</button>
        </div>
    );
}

export default ChatBox;

