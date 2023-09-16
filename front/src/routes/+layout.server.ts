/** @type {import('./$types').Actions} */

export const load = async({ cookies } : any) => {
    const user_connected = cookies.get('access');
    const user_role = cookies.get('role');
    const user_domain = cookies.get('domain');
  
    return {
      cookies_connexion : user_connected,
      cookies_role: user_role,
      cookies_domain: user_domain,
    }
}