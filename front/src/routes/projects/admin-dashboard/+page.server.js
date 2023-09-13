let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const load = async() => {

  console.log("Server Load Run");
  
  const fetchProjects = async () => {
    const res = await fetch(BASE_URL + '/assets');
    const data = await res.json();
    return data.all_asset;
  }

  return {
    projects: fetchProjects()
  }
}