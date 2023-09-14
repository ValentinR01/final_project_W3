<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import TextareaForm from "../../molecules/formFields/TextareaForm.svelte";
  import RadioForm from '../../molecules/formFields/RadioForm.svelte';
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";

  /**
   * @type {string}
  */
  export let radioValue;

  /**
   * @type {string}
  */
  export let selectValue;

  /**
   * @type {string}
  */
  export let selectValue2;

  /**
   * @type { any }
  */
  export let data; 

  const composers = data.composers;
  const composersList = composers.map((/** @type {{ fullname: string; }} */ item) => item.fullname);
  const intervenors = data.intervenors;
  const intervenorsList = intervenors.map((/** @type {{ fullname: string; }} */ item) => item.fullname);
  const instruments = data.instruments;
  const instrumentsList = intervenors.map((/** @type {{ value: string; }} */ item) => item.value);
  const categories = data.categories;
  const categoriesList = intervenors.map((/** @type {{ name: string; }} */ item) => item.name);

</script>

<form method="Post" action="?/create" class='form-projectCreation'>
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase'
  > 
    Création de projet
  </Text>
  <InputForm id='name-project' name='name-project'> Nom du projet </InputForm>
  <RadioForm data={categoriesList} catForm='categorie' bind:radioValue={radioValue}> Catégorie du projet </RadioForm>
  {#if radioValue == 'masterclass'}
    <SelectForm nameSelect="intervenor" options={intervenorsList} labelName='room' widthForm='calc(50% - 5px)' bind:selectValue={selectValue}> Nom de l'intervenant </SelectForm>
    <InputForm id='name-project' name='name-project' widthForm='calc(50% - 5px)'> Nom de l'étudiant </InputForm>
  {:else}
    <SelectForm nameSelect="intervenor" options={intervenorsList} labelName='room' bind:selectValue={selectValue}> Nom de l'intervenant </SelectForm>
  {/if}
  <CheckboxForm data={instrumentsList} catForm='instruments'> Instruments </CheckboxForm>
  <InputForm id='music-title' name='music-title' widthForm='calc(50% - 5px)'> Nom(s) du/des morceau(x) </InputForm>
  <SelectForm nameSelect="composer" options={composersList} labelName='room' widthForm='calc(50% - 5px)' bind:selectValue={selectValue2}> Compositeur </SelectForm>
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