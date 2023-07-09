import { error } from '@sveltejs/kit';
  
export function load() {
    return {
        users:[
            {
                id: 1,
                fullname: 'Chloé Doustalet',
                email: 'test@gmail.com',
                role: 'user',
                profile_pic: 'https://cdn.shopify.com/s/files/1/0442/6219/5368/files/3I3A1369-2.jpg?v=1685536090',
                count_assigning_asset: 3,
                domain: 'regisseur'
            },
            {
                id: 2,
                fullname: 'Nassim Yazi',
                email: 'nassim@gmail.com',
                role: 'admin',
                count_assigning_asset: 1,
                domain: 'traducteur'
            },
            {
                id: 3,
                fullname: 'Julia Doustalet',
                email: 'julia@gmail.com',
                role: 'admin',
                domain: 'editeur'
            },
            {
                id: 4,
                fullname: 'Doriane Farau',
                email: 'doriane@gmail.com',
                role: 'user',
                domain: 'post-prod'
            },
            {
                id: 5,
                fullname: 'Zoé Logeais',
                email: 'zoe@gmail.com',
                role: 'superadmin',
                domain: 'editeur'
            }
        ]
    };
}