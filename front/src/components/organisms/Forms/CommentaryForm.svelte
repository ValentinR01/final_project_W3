<script>
  import Button from "../../atoms/Button.svelte";
  import TextArea from "../../atoms/Text-Area.svelte";
  import InputForm from "../../molecules/formFields//InputForm.svelte";

  export let userComment = 'existing';
</script>

<form class="commentary-form">
  {#if userComment == 'new'}
    <InputForm id="name" name="name"> Nom </InputForm>
  {/if}
  <TextArea width='100%' placeholder="Ecrire un commentaire..." />
  <Button> Valider </Button>  
</form>

<style>
  .commentary-form{
    display: flex;
    flex-wrap: wrap;
    justify-content: end;
    row-gap: var(--spacing-2);
    width: 100%;
  }

  .commentary-form :global(textarea){
    padding: var(--spacing-3);
  }
</style>
