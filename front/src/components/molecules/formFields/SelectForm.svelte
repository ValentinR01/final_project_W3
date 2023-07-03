<script>
  import Select from "../../atoms/Select.svelte";

  export let name = '';
  export let nameSelect = "";
  export let widthForm = '100%';

  /**
   * @type {any}
   */
   export let data;

</script>

<div style="width: {widthForm}">
  <label for={name} class="text-preset-4"> <slot /> </label>
  <Select nameSelect={nameSelect} options={data}/>
</div>