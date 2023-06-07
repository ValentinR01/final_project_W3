<script>
  /**
  * @type {Array<string>}
  * */

  export let values;
</script>

{#each values as option}
  <input type=radio id={option} value={option} >
  <label for={option}> {option} </label>
{/each}