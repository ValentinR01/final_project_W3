<script>
  import Select from "../atoms/Select.svelte";

  /**
  * @type {Array<any>}
  */
  export let options;

  /**
  * @type {string}
  */
  export let nameSelect = '';
</script>

<div class="select-form">
  <label for={nameSelect} class="text-preset-4"> <slot /> </label>
  <Select nameSelect={nameSelect} options={options}/>
</div>

<style>
  .select-form{
    display: inline-grid;
    width: 100%;
  }

  label{
    margin-bottom: 5px;
  }
</style>