<script>
  import Input from "../atoms/Input.svelte";
  
  export let id = '';
  export let name = '';
  export let widthForm = '100%';
</script>

<div 
  class="input-form"
  style="width: {widthForm}"
>
  <label for={name} class="text-preset-4"> <slot /> </label>
  <Input name={name} id={id}/>
</div>

<style>
  .input-form{
    display: inline-grid;
  }

  label{
    margin-bottom: 5px;
  }
</style>