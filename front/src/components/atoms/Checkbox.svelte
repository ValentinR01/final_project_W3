<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
  * @type {any}
  */
  export let cat;
</script>
  
{#each values as option}
  <input type=checkbox id={option} value={option} name={cat}>
  <label for={option}> {option} </label>
{/each}