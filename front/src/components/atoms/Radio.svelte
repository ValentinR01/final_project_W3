<script>
/**
* @type {Array<string>}
*/

const getValues = [ "italien","anglais","français"]

</script>

{#each getValues as option}
<input type=radio id={option} value={option} >
<label for={option}> {option} </label>
{/each}