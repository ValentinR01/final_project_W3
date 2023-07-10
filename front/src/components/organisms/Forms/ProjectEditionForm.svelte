<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import TextareaForm from "../../molecules/formFields/TextareaForm.svelte";

  /**
   * @type {string}
  */
  export let selectValue;

  /**
   * @type {any}
  */
  export let data;

</script>

<form class="form-projectEdition">
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase'
  > 
    Edition projet 
  </Text>
  <InputForm id='name-project' name='name-project'> Nom du projet </InputForm>
  <TextareaForm> Description du projet </TextareaForm>
  <TextareaForm> Résumé </TextareaForm>
  <InputForm id='name-work' name='name-work'> Nom de l'oeuvre </InputForm>
  <TextareaForm> Description de l'oeuvre </TextareaForm>
  <CheckboxForm data={data.metadata.instruments} catForm='langues-traducteur'> Instruments </CheckboxForm>
  <InputForm id='duration' name='duration' type='number' widthForm='calc(50% - 5px)'> Durée (en min) </InputForm>
  <SelectForm nameSelect="language" data={data.metadata.translations} labelName='language' widthForm='calc(50% - 5px)' bind:selectValue={selectValue} > Langue </SelectForm>
  <CheckboxForm data={data.metadata.translations} catForm='langues-traducteur'> Langue(s) des sous-titres </CheckboxForm>
  <SelectForm nameSelect="duration" data={data.metadata.style} labelName='duration' widthForm='calc(50% - 5px)' bind:selectValue={selectValue}> Style de musique </SelectForm>
  <SelectForm nameSelect="language" data={data.metadata.era} labelName='language' widthForm='calc(50% - 5px)' bind:selectValue={selectValue}> Epoque </SelectForm>
  <SelectForm nameSelect="difficulty" data={data.metadata.rating} labelName='duration' widthForm='calc(50% - 5px)' bind:selectValue={selectValue}> Niveau de difficulté </SelectForm>
  <InputForm id='musical-store' name='musical-store' widthForm='calc(50% - 5px)'> Partition </InputForm>
  <Button marginTop='var(--spacing-2)'> Valider </Button>
</form>

<style>
  .form-projectEdition{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-3);
    column-gap: var(--spacing-2);
    justify-content: center;
  }
</style>