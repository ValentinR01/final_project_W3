<script>
  import Input from "../atoms/Input.svelte";
  
  export let id = '';
  export let name = '';
  export let type = '';
</script>

<div class="input-form">
  <label for={name} class="text-preset-4"> <slot /> </label>
  <Input name={name} id={id} type={type}/>
</div>

<style>
  .input-form{
    display: inline-grid;
    width: 100%;
  }

  label{
    margin-bottom: 5px;
  }
</style>