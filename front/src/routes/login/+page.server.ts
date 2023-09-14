/** @type {import('./$types').Actions} */
import { writable } from 'svelte/store'
import { redirect } from '@sveltejs/kit';
import { user } from '../../store';
let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const actions = {
    login: async ({ cookies, request } :any) => {
        const data = await request.formData();
        const username = data.get('username');
        const password = data.get('password');

        const res = await fetch(BASE_URL + 'users/login', {
          method: 'POST',
          headers: { 'Content-Type': `application/json` },
          body: JSON.stringify({
            "email" : username, 
            "password" : password})
        })

        if (res.status == 200){
          cookies.set("access", "true", { path: "/", sameSite: "strict"});
          user.set({ domain: 'traduction', role: 'superadmin', authentification: 'logged in'});
          throw redirect(302, '/projects/dashboard');
        }

        return {
          message: "Identifiants incorrects",
        }
    }
};
