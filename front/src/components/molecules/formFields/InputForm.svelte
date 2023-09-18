<script>
  import Input from "../../atoms/Input.svelte";
  
  export let id = '';
  export let name = '';
  export let type = 'text';
  export let placeholder = "";
  export let widthForm = '100%';
  export let valueInput = "";
  export let readonly = false;
  export let required = false; 
</script>

<div 
  class="input-form"
  style="width: {widthForm}"
>
  <label for={name} class="input-form__label text-preset-4"> <slot /> </label>
  {#if readonly}
    <Input name={name} id={id} type={type} placeholder={placeholder} bind:inputValue={valueInput} width=auto readonly/>
  {:else if required}
    <Input name={name} id={id} type={type} placeholder={placeholder} bind:inputValue={valueInput} width=auto required/>
  {:else}
    <Input name={name} id={id} type={type} placeholder={placeholder} bind:inputValue={valueInput} width=auto/>
  {/if}
</div>

<style>
  .input-form{
    display: inline-grid;
  }

  .input-form__label{
    margin-bottom: var(--spacing-1);
  }
</style>