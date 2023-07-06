<script>
  import Input from "../../atoms/Input.svelte";
  
  export let id = '';
  export let name = '';
  export let widthForm = '100%';
</script>

<div 
  class="input-form"
  style="width: {widthForm}"
>
  <label for={name} class="input-form__label text-preset-4"> <slot /> </label>
  <Input name={name} id={id} width=auto/>
</div>

<style>
  .input-form{
    display: inline-grid;
  }

  .input-form__label{
    margin-bottom: var(--spacing-1);
  }
</style>