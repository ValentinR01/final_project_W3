export function load() {
    return {
        metadata:{
            instruments: ["piano","violon","guitare","violoncelle","trombone","harpe","trompette","flute"],
            categorie: ["concert", "interview", "masterclass"],
            rating: [1,2,3,4],
            role: ["superadmin","admin","user"], 
            domain: ["post-prod","regisseur","traducteur","editeur"], 
            translations: ["Français","Anglais","Italien","Espagnol","Allemand","Japonais","Russe","Arabe","Chinois","Coréen","Portugais"],
            style: ["classical","jazz","medieval"],
            era: ["XII","XVI","XVIII","XIX","XX"]
        },
        projects: [
            {
                id: 1,
                name: "Interview 1",
                instruments: ["piano","violon","guitare"],
                categorie: "interview",
                rating: 3,
                translations: ["Français","Anglais"]
            },
            {
                id: 2,
                name: "Interview 2",
                instruments: ["piano","violon","guitare"],
                categorie: "interview",
                rating: 4,
                translations: ["Français","Allemand"]
            },
            {
                id: 3,
                name: "Concert de Jean Mich",
                instruments: ["piano","violon","guitare"],
                categorie: "concert",
                rating: 1,
                translations: ["Russe","Espagnol","Chinois"]
            },
            {
                id: 4,
                name: "Concert de Sabine Wesh",
                instruments: ["piano","trombone"],
                categorie: "concert",
                rating: 1
            },
            {
                id: 5,
                name: "Masterclass sur la mélodie romantique",
                instruments: ["piano","violon","guitare"],
                categorie: ["masterclass", "concert", "interview"],
                rating: 5
            },
            {
                id: 6,
                name: "Masterclass sur l'intensité de jeu",
                instruments: ["piano","violon","violoncelle"],
                categorie: "masterclass",
                rating: 3
            }
        ],
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
        ],
        booking:{
            room: [ 'Salle 1', 'Salle 2', 'Salle 3' ],
            time_slot: ['8h - 10h', '10h - 12h', '12h - 14h', '14h - 16h', '16h - 18h', '18h - 20h']
        },
        composer:[ "Compositeur 1","Compositeur 2","Compositeur 3","Compositeur 4","Compositeur 5" ],
        intervenor:[ "Intervenant 1","Intervenant 2","Intervenant 3","Intervenant 4","Intervenant 5" ],
    };
}