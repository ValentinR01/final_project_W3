// @ts-nocheck
/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
  const res = await fetch(`http://127.0.0.1:8004/api/v1/users`);
  const item = await res.json();

  return { item };
}