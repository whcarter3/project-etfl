'use client';

import { supabase } from '../lib/supabaseClient';

export default function Login() {
  const handleLogin = async () => {
    const { error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
    });
    if (error) {
      console.error('Error logging in:', error.message);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <button
        onClick={handleLogin}
        className="px-4 py-2 bg-blue-500 text-white rounded-md"
      >
        Sign in with Google
      </button>
    </div>
  );
}
