/** @type {import('./$types').Actions} */
import { redirect } from '@sveltejs/kit';
//import { BASE_URL } from '$env/static/private';
let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const actions = {
  register: async ({ request } : any) => {
    const data = await request.formData();
    const fullname = data.get('fullname');
    const email = data.get('email');
    const password = data.get('password');
    const domain = data.get('domain');
    const role = data.get('role');
    
    const res = await fetch(BASE_URL + '/users/register', {
      method: 'POST',
      headers: { 'Content-Type': `application/json` },
      body: JSON.stringify({
        "fullname" : fullname, 
        "email" : email, 
        "password" : password,
        "domain_id": 1,
        "role_id": 1
      })
    })
    
    if (res.status == 201){
      throw redirect(302, '/users/dashboard');
    }
  },
};

// REMPLACER AVEC LES BONS ENDPOINTS
export const load = async() => {
  console.log("Server Load Run");
  const fetchDomains = async () => {
    const res = await fetch(BASE_URL + '');
    const data = await res.json();
    return data;
  }

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
    //domains: fetchDomains(),
    //roles: fetchRoles(),
    // A CHANGER UNE FOIS QUE L'ON A LES BONS ENDPOINTS
    domains: [{"id":1, "name":"traducteur"},{"id":2, "name":"regisseur"},{"id": 3, "name":"post-prod"}],
    roles: [{"id": 1, "name":"superadmin"},{"id": 2, "name":"admin"},{"id": 3, "name":"user"}],
    translations: fetchTranslations(),
  }
}