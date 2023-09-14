/** @type {import('./$types').Actions} */
import { redirect } from '@sveltejs/kit';
let BASE_URL = 'http://dam-backoffice-api:8000/api/v1/';

export const actions = {
  create: async ({ request } : any) => {
    const data = await request.formData();
    const title = data.get('title');
    const music_title = data.get('music-title');
    const speaker_id = 1;
    const composer_id = 1;
    // TO CHANGE AFTER LOGIN DATA GOTTEN
    const created_by_id = 1;
    const updated_by_id = 1;
    const status_by_domain_id = 1;
    // AJOUT DU RENVOI DES INSTRUMENTS

    const asset_id = 1;
    
    const res = await fetch(BASE_URL + '/assets/create', {
      method: 'POST',
      headers: { 'Content-Type': `application/json` },
      body: JSON.stringify({
        "title" : title, 
        "music_title" : music_title, 
        "created_by_id" : created_by_id,
        "updated_by_id": updated_by_id,
        "status_by_domain_id": status_by_domain_id,
        "step_lifecycle_id" : 1,
        "speaker_id": speaker_id,
        "composer_id": composer_id
      })
    })

    //const res2 = await fetch(BASE_URL + '/assets/' + asset_id + '/comments', {
    //  method: 'POST',
    //  headers: { 'Content-Type': `application/json` },
    //  body: JSON.stringify({
    //    "title" : title, 
    //    "music_title" : music_title, 
    //    "created_by_id" : created_by_id,
    //    "updated_by_id": updated_by_id,
    //    "status_by_domain_id": status_by_domain_id,
    //    "step_lifecycle_id" : 1
    //  })
    //})
    
    if (res.status == 201){
      throw redirect(302, '/users/dashboard');
    }
  },
};

export const load = async() => {
  console.log("Server Load Run");

  const fetchComposers = async () => {
    const res = await fetch(BASE_URL + 'composers');
    const data = await res.json();
    return data.composers;
  }

  const fetchIntervenors = async () => {
    const res = await fetch(BASE_URL + 'speakers');
    const data = await res.json();
    return data.speakers;
  }

  const fetchInstruments =  async () => {
    const res = await fetch(BASE_URL + 'meta_value?meta_key=instruments');
    const data = await res.json();
    return data.meta_values;
  }

  const fetchCategories =  async () => {
    const res = await fetch(BASE_URL + 'categories');
    const data = await res.json();
    return data.categories;
  }

  return {
    composers: fetchComposers(),
    intervenors: fetchIntervenors(),
    instruments: fetchInstruments(),
    categories: fetchCategories(),
  }
}