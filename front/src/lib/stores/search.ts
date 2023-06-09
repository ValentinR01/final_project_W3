import { writable } from "svelte/store"

export const createSearchStore = (data:any) => {
	const { subscribe, set, update } = writable({
		data: data,
		filtered: data,
		search: "",
	})

	return {
		subscribe,
		set,
		update,
	}
}

export const searchHandler = (store:any) => {
	const searchTerm = store.search.toLowerCase() || ""
	store.filtered = store.data.filter((item:any) => {
		console.log(searchTerm);
		console.log(item.searchTerms);
		return item.searchTerms.toLowerCase().includes(searchTerm)
	})
}