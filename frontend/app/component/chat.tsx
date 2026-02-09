"use client";

import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>(
    [],
  );
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input) return;
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    // Call backend API
    const res = await fetch("http://127.0.0.1:8000/agent/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: input,
        user_id: "sahil@example.com", // replace with login user
        thread_id: "thread_1",
      }),
    });

    const data = await res.json();
    const replyContent = data.reply || JSON.stringify(data);

    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: replyContent },
    ]);
    setLoading(false);
  };

  return (
    <div className="max-w-2xl mx-auto p-4 border rounded-md shadow-md">
      <div className="h-80 overflow-y-auto mb-4 flex flex-col gap-2">
        {messages.map((m, i) => (
          <div
            key={i}
            className={m.role === "user" ? "text-right" : "text-left"}
          >
            <span
              className={`inline-block p-2 rounded-md ${m.role === "user" ? "bg-blue-500 text-white" : "bg-gray-200"}`}
            >
              {m.content}
            </span>
          </div>
        ))}
        {loading && <div className="text-left text-gray-400">Thinking...</div>}
      </div>
      <div className="flex gap-2">
        <input
          type="text"
          className="flex-1 p-2 border rounded-md"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type your question..."
        />
        <button
          className="px-4 py-2 bg-blue-600 text-white rounded-md"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
}
