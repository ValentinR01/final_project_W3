<script>
  /**
   * @type {any[]}
  */
  export let items = [];
  export let activeTabValue = 1;

  /**
   * @type {any}
  */
  export let data; 
 
  const handleClick = (/** @type {number} */ tabValue) => () => (activeTabValue = tabValue);
</script>

<div class="tabs">
  <ul>
    {#each items as item}
      <li class={activeTabValue === item.value ? 'active' : ''}>
  	  <span class="text-preset-3" on:click={handleClick(item.value)}>{item.label}</span>
      </li>
    {/each}
  </ul>
   
  {#each items as item}
    {#if activeTabValue == item.value}
      <div class="box">
  	    <svelte:component this={item.component} data={data} />
      </div>
    {/if}
  {/each}

</div>
 
 <style>
  .box {
	padding: 40px;
  }

  ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
  }

  li {
	padding: 0 var(--spacing-4) var(--spacing-2) var(--spacing-1);
	border-bottom: 1px solid var(--color-border);
  }
 
  span {
    display: block;
    cursor: pointer;
	color: var(--color-text-dark);
  }
   
  span:hover {
    border-color: #e9ecef #e9ecef #dee2e6;
  }
   
  li.active > span {
    color: var(--color-primary);
  }

  li.active{
    border-color: var(--color-primary);
  }
</style>