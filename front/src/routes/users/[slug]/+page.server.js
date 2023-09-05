export const load = async() => {
  console.log("Server Load Run");
  const fetchUser = async () => {
    const res = await fetch('http://dam-backoffice-api:8000/api/v1/users?id=1');
    const data = await res.json();
    return data.user;
  }

  return {
    user: fetchUser(),
  }
}