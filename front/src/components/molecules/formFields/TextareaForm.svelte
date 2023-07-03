<script>
  import TextArea from "../../atoms/Text-Area.svelte";

  export let name = '';
  export let placeholder = '';
  export let widthForm = '100%';

</script>
  
<div 
  class="textarea-form" 
  style="width: {widthForm}"
>
  <label for={name} class="text-preset-4"> <slot /> </label>
  <TextArea placeholder={placeholder} />
</div>

<style>
  .textarea-form{
    display: inline-grid;
  }

  label{
    margin-bottom: 5px;
  }
</style>