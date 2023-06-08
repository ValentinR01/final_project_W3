<script>
    export let type = 'text';
    export let id = '';
    export let name = '';
    export let placeholder = 'Votre texte...';
</script>

<input 
  type={type}
  id={id} 
  name={name} 
  placeholder={placeholder}
  class="input text-preset-5 {$$props.class}"
/>

<style>
  .input{
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
    border-radius: var(--color-disabled);
    padding: var(--spacing-2);
    min-width: 280px;
    font-family: var(--font-family-primary);
    border-radius: var(--small-radius);
  }

  input::placeholder{
    font-size: var(--font-size-label-1);
    font-family: var(--font-family-primary);
  }

  .input:focus {
    color: var(--color-primary);
  }

  .input:focus-visible {
    outline: var(--border-height-regular) solid var(--color-highlight);
    outline-offset: -1px;
  }

  .input-valid {
      border: var(--border-height-thick) solid var(--color-highlight);
  }

  .input-invalid {
    border: var(--border-height-thick) solid #FF4D4D;
  }

</style>
