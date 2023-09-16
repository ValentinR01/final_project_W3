<script lang="ts">
	import TableRowProjects from '../molecules/TableRowProjects.svelte';
  import Icon from '../atoms/Icon.svelte';
  import SortArrowIcon from '../../assets/icons/SortArrowIcon.svelte';

	export let selectedRowElements : any;

  const tableHeaders = Object.keys(selectedRowElements[0])

  let selectedHeader = "";
  let ascendingOrder = true;

  const sortByNumber = (keyHeader: any) => {
    selectedRowElements = selectedRowElements.sort((obj1: any, obj2: any) => {
      return ascendingOrder ? Number(obj1[keyHeader]) - Number(obj2[keyHeader])
      : Number(obj2[keyHeader]) - Number(obj1[keyHeader])
    });
    selectedHeader = keyHeader;
  }

  const sortByString = (colHeader: any) => {
    selectedRowElements = selectedRowElements.sort((obj1: any, obj2: any) => {
      if (obj1[colHeader] < obj2[colHeader]) {
          return -1;
      } else if (obj1[colHeader] > obj2[colHeader]) {
        return 1;
      }
      return 0;	
    });
    if (!ascendingOrder) {
      selectedRowElements = selectedRowElements.reverse()
    }
    selectedHeader = colHeader;
  }
  let motSpecifique = "has_high_priority";
</script>

<table>
	<thead>
    <tr> 
      {#each tableHeaders as header}
      <th class:text-center={header.includes(motSpecifique)} on:click={() => (header === "has_high_priority" || header === "rush_received" || header === "captation_done" ) ? sortByNumber(header) : sortByString(header)}>
        <button on:click={() => ascendingOrder = !ascendingOrder}>
          {header
          .replace("title", "Projet")
          .replace("has_high_priority", "Priorité")
          .replace("categorie", "Catégorie")
          .replace("language", "Langue")
          .replace("created_at", "Créé le")
          .replace("step_lifecycle", "Étape")
          .replace("published_at", "Mise en ligne")
          .replace("last_assignment_date", "Attribué le")
          .replace("name_by_domain", "Personne")
          .replace("rush_received", "Rushes récupérés")
          .replace("version", "Version")
          .replace("captation_done", "Captation réalisée")}
          <span>
            <Icon color="var(--darker-grey)" width="10" height="12">
              <SortArrowIcon />
            </Icon>
          </span>		
        </button>	
      </th>
      {/each}
    </tr>
  </thead>
  <tbody>
	  <TableRowProjects {selectedRowElements}/>
	</tbody>
</table>

<style>
  .text-center {
    /* Styles pour la classe ajoutée */
   text-align: center;
  }
  table {
    margin: auto;
    width: 100%;
  }
  tr {
    white-space: nowrap;
  }
  th {
    padding-bottom: var(--spacing-3);
    padding-left: var(--spacing-4);
    padding-right: var(--spacing-4);
    text-align: left;
  }
  th:first-child {
    padding-left: 0;
  }
  span {
    display: inline-block;
    vertical-align: middle;
    margin-left: var(--spacing-1);
  }
  button {
    cursor: pointer;
    border: none;
    margin: 0;
    padding: 0;
    width: auto;
    overflow: visible;
    background: transparent;
    color: var(--darker-grey);
    font: inherit;
    line-height: normal;
    -webkit-font-smoothing: inherit;
    -moz-osx-font-smoothing: inherit;
    -webkit-appearance: none;
  }
</style>