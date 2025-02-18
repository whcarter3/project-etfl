'use client';
import { useState } from 'react';
import { fetchYahooLeagues } from '@/app/lib/api';

export default function Home() {
  const [leagues, setLeagues] = useState(null);
  const [token, setToken] = useState('');

  const getLeauges = async () => {
    const data = await fetchYahooLeagues(token);
    setLeagues(data);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter your Yahoo access token"
        value={token}
        onChange={(e) => setToken(e.target.value)}
        className="p-2 border"
      />
      <button
        onClick={getLeauges}
        className="ml-2 p-2 bg-blue-500 text-white"
      >
        Fetch Leagues
      </button>
      <pre>{JSON.stringify(leagues, null, 2)}</pre>
    </div>
  );
}
