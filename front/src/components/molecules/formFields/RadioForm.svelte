<script>
  import Radio from "../../atoms/Radio.svelte";

  export let name = '';
  export let catForm = "";
  export let widthForm = '100%';

  /**
   * @type {any}
   */
   export let data;

</script>

<div style="width: {widthForm}">
  <label for={name} class="text-preset-4 radioForm-label"> <slot /> </label>
  <Radio values={data} cat={catForm}/>
</div>

<style>
  .radioForm-label{
    display: block;
    padding-bottom: var(--spacing-1);
  }
</style>