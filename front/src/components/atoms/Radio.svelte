<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
  * @type {String}
  */
  export let cat;
</script>

{#each values as option}
  <input type=radio id={option} value={option} name={cat}>
  <label for={option}> {option} </label>
{/each}