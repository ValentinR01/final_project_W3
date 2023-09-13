let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const load = async({ params }: any) => {

  console.log("Server Load Run");
  
  const fetchUser = async () => {
    const res = await fetch(BASE_URL + '/users/' + params.slug);
    const data = await res.json();
    return data;
  }

  const fetchDomains = async () => {
    const res = await fetch(BASE_URL + '/domains');
    const data = await res.json();
    return data.all_domain;
  }

  const fetchRoles = async () => {
    const res = await fetch(BASE_URL + '/roles');
    const data = await res.json();
    return data.all_role;
  }

  const fetchTranslations = async () => {
    const res = await fetch(BASE_URL + 'languages');
    const data = await res.json();
    return data.languages;
  }

  return {
    user: fetchUser(),
    translations: fetchTranslations(),
    domains: fetchDomains(),
    roles: fetchRoles(),
  }
}