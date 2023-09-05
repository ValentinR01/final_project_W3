let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const load = async({ params }: any) => {

  console.log("Server Load Run");
  const fetchUser = async () => {
    const res = await fetch(BASE_URL + '/users/' + params.slug);
    const data = await res.json();
    return data;
  }

  // REMPLACER AVEC LES BONS ENDPOINTS
  const fetchDomains = async () => {
    const res = await fetch(BASE_URL + '');
    const data = await res.json();
    return data;
  }

  // REMPLACER AVEC LES BONS ENDPOINTS
  const fetchRoles = async () => {
    const res = await fetch(BASE_URL + '');
    const data = await res.json();
    return data;
  }

  const fetchTranslations = async () => {
    const res = await fetch(BASE_URL + 'languages');
    const data = await res.json();
    return data.languages;
  }

  return {
    user: fetchUser(),
    translations: fetchTranslations(),
    //domains: fetchDomains(),
    //roles: fetchRoles(),
    // A CHANGER UNE FOIS QUE L'ON A LES BONS ENDPOINTS
    domains: [{"id":1, "name":"traducteur"},{"id":2, "name":"regisseur"},{"id": 3, "name":"post-prod"}],
    roles: [{"id": 1, "name":"superadmin"},{"id": 2, "name":"admin"},{"id": 3, "name":"user"}],
  }
}