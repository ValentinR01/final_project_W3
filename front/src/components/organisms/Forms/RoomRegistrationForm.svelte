<script>
  import Button from "../../atoms/Button.svelte";
  import DatePicker from "../../atoms/DatePicker.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";

  /**
   * @type { any }
  */
  export let data; 

</script>

<form class='form-room'>
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase'
  > 
    Interview de Laure Sulob
  </Text>
  <SelectForm nameSelect="duration" data={data.room} labelName='room' > Choix de la salle </SelectForm>
  <div class='form-datePicker'>
    <label for='date' class="text-preset-4 form-datePicker__label"> Choix de la salle </label>
    <DatePicker />
  </div>
  <SelectForm nameSelect="time-slot" data={data.time_slot} labelName='time-slot' widthForm='calc(50% - 5px)' > Choix du créneau </SelectForm>
  <Button marginTop='var(--spacing-2)'> Confirmer </Button>
</form>

<style>
  .form-room{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    row-gap: var(--spacing-3);
    column-gap: var(--spacing-2);
  }

  .form-datePicker{
    display: flex;
    flex-wrap: wrap;
    width: calc(50% - 5px);
  }

  .form-datePicker__label{
    width: 100%;
    margin-bottom: var(--spacing-1);
  }
</style>