<script>
  import Select from "../../atoms/Select.svelte";

  export let labelName = "";
  export let nameSelect = "";
  export let widthForm = '100%';

  export let selectValue;

  /**
   * @type {any}
  */
  export let data;

</script>

<div class="select-form" style="width: {widthForm}">
  <label for={labelName} class="select-form__label text-preset-4"> <slot /> </label>
  <Select nameSelect={nameSelect} options={data} bind:valueSelected={selectValue}/>
</div>

<style>
  .select-form__label{
    display: inline-block;
    margin-bottom: var(--spacing-1);
  }
</style>