export async function fetchYahooLeagues(accessToken: string) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/yahoo/leagues?access_token=${accessToken}`
    //pass along access token as a string
  );

  return response.json();
}
