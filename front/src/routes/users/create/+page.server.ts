/** @type {import('./$types').Actions} */
import { redirect } from '@sveltejs/kit';
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

export const load = async() => {
  console.log("Server Load Run");
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
    domains: fetchDomains(),
    roles: fetchRoles(),
    translations: fetchTranslations(),
  }
}