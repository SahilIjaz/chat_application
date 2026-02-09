async function getHealth() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/`);
  return res.json();
}

import Chat from "./component/chat";

export default async function Home() {
  const data = await getHealth();

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">Omni-Agent Dashboard</h1>
      <Chat />
      <pre className="bg-gray-100 p-4 rounded">
        {JSON.stringify(data, null, 2)}
      </pre>
    </main>
  );
}
