import Chat from "./component/chat";

export default function Home() {
  return (
    <main className="min-h-screen bg-black flex items-center justify-center p-6">
      <div className="w-full max-w-3xl mx-auto">
        <div className="bg-gray-900 border border-gray-700 rounded-lg shadow-md overflow-hidden">
          <div className="px-6 py-4 border-b border-gray-700">
            <h1 className="text-2xl font-bold text-white">AgentFlow</h1>
            <p className="text-sm text-gray-400">AI-Powered Agent Chat Platform</p>
          </div>
          <div className="p-6">
            <Chat />
          </div>
        </div>
      </div>
    </main>
  );
}
