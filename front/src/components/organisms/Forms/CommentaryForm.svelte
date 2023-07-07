<script>
  import Button from "../../atoms/Button.svelte";
  import TextArea from "../../atoms/Text-Area.svelte";
</script>

<form class="commentary-form">
  <TextArea placeholder="Ecrire un commentaire..." />
  <Button marginTop="var(--spacing-2)"> Valider </Button>  
</form>

<style>
  .commentary-form{
    display: flex;
    flex-wrap: wrap;
    justify-content: end;
  }

  .commentary-form :global(textarea){
    padding: var(--spacing-3);
  }
</style>