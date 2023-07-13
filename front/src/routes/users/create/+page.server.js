/** @type {import('./$types').Actions} */
import { redirect } from '@sveltejs/kit';
//import { BASE_URL } from '$env/static/private';
let BASE_URL = 'http://localhost:8004/api/v1';

export const actions = {
  register: async ({ request }) => {
    const data = await request.formData();
    const fullname = data.get('fullname');
    const email = data.get('email');
    const password = data.get('password');
    
    const res = await fetch(BASE_URL + '/users/register', {
      method: 'POST',
      headers: { 'Content-Type': `application/json` },
      body: JSON.stringify({
        "fullname" : 'testChloé', 
        "email" : 'testchloe@saline.com', 
        "password" : 'testChloé',
        "domain_id": 1,
        "role_id": 1
      })
    })
    
    if (res.status == 201){
      throw redirect(302, '/users/dashboard');
    }
  },
};

