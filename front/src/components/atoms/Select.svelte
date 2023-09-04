<script>
  /**
  * @type {Array<any>}
  */
  export let options = [];

  /**
  * @type {String}
  */
  export let nameSelect = '';

  /**
  * @type {any}
  */
  export let valueSelected = options[0];
  let value;

  $: {
    value = valueSelected;
  }
</script>


<div class="select-wrapper">
  <select 
    name={nameSelect}
    bind:value={valueSelected}
  >
    {#each options as option}
      <option value={option}>{option}</option>
    {/each}
  </select>
</div>

<style>
  
  select{
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 40px;
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
    border-radius: var(--color-disabled);
    padding: var(--spacing-2);
    padding-right: var(--spacing-4);
    font-family: var(--font-family-primary);
    font-weight: var(--font-weight-light);
    border-radius: var(--small-radius);
    text-align: center;
    text-transform: capitalize;
  }

  .select-wrapper {
    position: relative;
  }

  .select-wrapper::after {
    content: url(//cdn.shopify.com/s/files/1/0442/6219/5368/t/58/assets/arrow-down.svg?v=1797229…);
    font-size: 1rem;
    top: 10px;
    right: 15px;
    position: absolute;
  }

</style>
