export function load() {
    return {
        metadata:{
            instruments: ["piano","violon","guitare","violoncelle","trombone","harpe","trompette","flute"],
            categorie: ["masterclass", "concert", "interview"],
            rating: [1,2,3,4],
            role: ["superadmin","admin","user"]
        },
        projects: [
            {
                id: 1,
                name: "Interview 1",
                instruments: ["piano","violon","guitare"],
                categorie: "interview",
                rating: 3
            },
            {
                id: 2,
                name: "Interview 2",
                instruments: ["piano","violon","guitare"],
                categorie: "interview",
                rating: 4
            },
            {
                id: 3,
                name: "Concert de Jean Mich",
                instruments: ["piano","violon","guitare"],
                categorie: "concert",
                rating: 1
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
                role: 'user'
            },
            {
                id: 2,
                fullname: 'Nassim Yazi',
                email: 'nassim@gmail.com',
                role: 'admin'
            },
            {
                id: 3,
                fullname: 'Julia Doustalet',
                email: 'julia@gmail.com',
                role: 'admin'
            },
            {
                id: 4,
                fullname: 'Doriane Farau',
                email: 'doriane@gmail.com',
                role: 'user'
            },
            {
                id: 5,
                fullname: 'Zoé Logeais',
                email: 'zoe@gmail.com',
                role: 'superadmin'
            }
        ]
    };
}