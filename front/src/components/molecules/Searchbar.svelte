<script lang="ts">
	import { createSearchStore, searchHandler } from '../../lib/stores/search';
	import { onDestroy } from 'svelte';
  import Icon from '../atoms/Icon.svelte';
  import SearchIcon from '../../assets/icons/SearchIcon.svelte';
  import Input from '../atoms/Input.svelte';
  import Link from '../atoms/Link.svelte';

  export let widthSearchbar = "200";
  export let urlSearchbar = "projects";
	export let data;

	const searchItems = data.map((item: any) => ({
		...item,
		searchTerms: `${item.name} ${item.fullname}` 
	}));

	const searchStore = createSearchStore(searchItems);

	const unsubscribe = searchStore.subscribe((model) => searchHandler(model));

	onDestroy(() => {
		unsubscribe();
	});
</script>

<div class="searchbar-container" style="width:{widthSearchbar}px">
  <div class="searchbar__field">
    <Input 
      type='search' 
      id='search' 
      name='search'
      class='input-with-icon'
      width='100%';
      bind:value={$searchStore.search} 
    /> 

    <Icon 
      name='search' 
      width="25" 
      height="15"
      class='input-icon'
    >
      <SearchIcon />
    </Icon>
  </div>

  <div class="searchbar__results">
  	{#each $searchStore.filtered as item}
      <div class="searchbar__list">
        <Link
          linkUrl='/{urlSearchbar}/{item.id}'
          linkColor='grey'
        > 
          {#if urlSearchbar === 'projects'}
            {item.name}
          {:else if urlSearchbar === 'users' }
            {item.fullname}
          {/if }
        </Link>
      </div>
  	{/each}
  </div>
</div>

<style>
  .searchbar__field{
    position: relative;
  }

  .searchbar__results{
    background-color: var(--color-background-secondary);
  }

  .searchbar__list{
    padding: 10px 10px;
  }
</style>
