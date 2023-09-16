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

        console.log(res.status);

        if (res.status == 200){
          // TO DO : change by real data of the user
          sessionStorage.setItem("role", "superadmin");
          sessionStorage.setItem("domain", "traduction");
          cookies.set("access", "true", { path: "/", sameSite: "strict"});
          cookies.set("role", "superadmin", { path: "/", sameSite: "strict"});
          cookies.set("domain", "traduction", { path: "/", sameSite: "strict"});
          throw redirect(302, '/projects/admin-dashboard');
        }

        return {
          formSubmitted,
          message: "Identifiants incorrects",
        }
    }
};
