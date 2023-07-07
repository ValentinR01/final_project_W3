<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import TextareaForm from "../../molecules/formFields/TextareaForm.svelte";
  import RadioForm from '../../molecules/formFields/RadioForm.svelte';
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";

  /**
   * @type { any }
  */
  export let data; 

  export let radioValue;

  let selectedValue;
  let showStudent = false;

  const handleSelection = () => {
    console.log('TEST');
    showStudent = selectedValue === 'masterclass';
  };
</script>

<form class='form-projectCreation'>
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase'
  > 
    Création de projet
  </Text>

  <InputForm id='name-project' name='name-project'> Nom du projet </InputForm>
  <RadioForm data={data.metadata.categorie} catForm='categorie' bind:radioValue={radioValue}> Catégorie du projet </RadioForm>
  {#if radioValue == 'masterclass'}
    <SelectForm nameSelect="duration" data={data.intervenor} labelName='room' widthForm='calc(50% - 5px)'> Nom de l'intervenant </SelectForm>
    <InputForm id='name-project' name='name-project' widthForm='calc(50% - 5px)'> Nom de l'étudiant </InputForm>
  {:else}
    <SelectForm nameSelect="duration" data={data.intervenor} labelName='room'> Nom de l'intervenant </SelectForm>
  {/if}
  <CheckboxForm data={data.metadata.instruments} catForm='langues-traducteur'> Instruments </CheckboxForm>
  <InputForm id='name-project' name='name-project' widthForm='calc(50% - 5px)'> Nom(s) du/des morceau(x)t </InputForm>
  <SelectForm nameSelect="duration" data={data.composer} labelName='room' widthForm='calc(50% - 5px)'> Compositeur </SelectForm>
  <TextareaForm> Commentaire </TextareaForm>
  
  <Button> Valider </Button>
</form>

<style>
  .form-projectCreation{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-3);
    column-gap: var(--spacing-2);;
    justify-content: center;
  }
</style>