<script>
  import Checkbox from "../../atoms/Checkbox.svelte";

  export let name = '';
  export let catForm = "";
  export let widthForm = '100%';

  /**
   * @type {string[]}
  */
  export let disabled = [];
  
  /**
   * @type {string[]}
   */
   export let optionsSelected = [];

  /**
   * @type {any}
  */
  export let data;

</script>

<div style="width: {widthForm}">
  <label for={name} class="text-preset-4 checkboxForm-label"> <slot /> </label>
  <Checkbox 
    values={data} 
    cat={catForm} 
    disabled={disabled}
    bind:selectedOptions={optionsSelected}
  />
</div>

<style>
  .checkboxForm-label{
    display: block;
    padding-bottom: var(--spacing-2);
  }
</style>