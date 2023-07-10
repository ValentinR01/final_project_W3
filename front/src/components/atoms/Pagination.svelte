<script>
  import Icon from "./Icon.svelte";
  import ArrowRightIcon from "../../assets/icons/ArrowRightIcon.svelte";
  import ArrowLeftIcon from "../../assets/icons/ArrowLeftIcon.svelte";
  
  /**
   * @type {string | any[]}
  */
  export let rows;
  
  /**
   * @type {number}
  */
  export let perPage;
  export let trimmedRows;  

  $: totalRows = rows.length 
  $: currentPage = 0
  $: totalPages = Math.ceil(totalRows / perPage) 
  $: start =  currentPage * perPage
  $: end = currentPage === totalPages - 1 ? totalRows - 1 : start + perPage - 1  ;

  $: trimmedRows = rows.slice(start, end + 1); 

  $: totalRows, currentPage = 0
  $: currentPage, start, end

</script>

{#if totalRows && totalRows > perPage}
  <div class='pagination'>
    <button on:click={() => currentPage -= 1}
      class="pagination-nav button--transparent"
      disabled={currentPage === 0 ? true : false} 
      aria-label="left arrow icon" 
      aria-describedby="prev">
      <Icon name="arrow" color='transparent' width="10" height="10">
        <ArrowLeftIcon />
      </Icon>
    </button>
    <span id='prev' class='sr-only'>Load previous {perPage} rows</span>
    <p class="text-preset-5"> <span class="text--semibold"> {currentPage + 1} </span> - {totalPages}</p>
    <button on:click={() => currentPage += 1} 
      class="pagination-nav button--transparent"
      disabled={currentPage === totalPages - 1 ? true : false} 
      aria-label="right arrow icon" 
      aria-describedby="next">
      <Icon name="arrow" color='transparent' width="10" height="10">
        <ArrowRightIcon />
      </Icon>
    </button>
    <span id='next' class='sr-only'>Load next {perPage} rows</span>
  </div>
{/if}

<style>
  .sr-only{
    position: absolute;
    clip: rect(1px, 1px, 1px, 1px);
    padding: 0;
    border: 0;
    height: 1px;
    width: 1px;
    overflow: hidden;
  }
  
  .pagination{
    display: flex;
    align-items: baseline;
    justify-content: end;
    pointer-events: all;
  }

  .pagination p{
    margin: 0 7px 0 5px;
  }

</style>