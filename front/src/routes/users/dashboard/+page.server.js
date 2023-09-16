export const load = async() => {
  console.log("Server Load Run");
  const fetchUsers = async () => {
    const res = await fetch('http://dam-backoffice-api:8000/api/v1/users');
    const data = await res.json();
    return data.users;
  }

  return {
    users: fetchUsers(),
  }
}