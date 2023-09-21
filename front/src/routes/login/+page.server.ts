/** @type {import('./$types').Actions} */
import { redirect } from '@sveltejs/kit';
let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const actions = {
    login: async ({ cookies, request } :any) => {
        const data = await request.formData();
        const username = data.get('username');
        const password = data.get('password');
        const formSubmitted = true;

        const res = await fetch(BASE_URL + 'users/login', {
          method: 'POST',
          headers: { 'Content-Type': `application/json` },
          body: JSON.stringify({
            "email" : username, 
            "password" : password})
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          cookies.set("access", "true", { path: "/", sameSite: "strict"});
          cookies.set("role", data.user.role, { path: "/", sameSite: "strict"});
          cookies.set("domain", data.user.domain, { path: "/", sameSite: "strict"});
          cookies.set("id", data.user.id, { path: "/", sameSite: "strict"});
          throw redirect(302, '/projects/admin-dashboard');
        })

        return {
          formSubmitted,
          message: "Identifiants incorrects",
        }
    }
};
