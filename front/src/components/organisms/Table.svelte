<script lang="ts">
	import TableRow from '../molecules/TableRow.svelte';
  import Icon from '../atoms/Icon.svelte';
  import SortArrowIcon from '../../assets/icons/SortArrowIcon.svelte';

	export let rowElements : any;

	let selectedRowElements = rowElements.map((
    {title, has_high_priority, categorie, language, created_at, status_by_domain, published_at, last_assignment_date, name_by_domain, rush_received, version, captation_done}: any) => ({ title, has_high_priority, categorie, language, created_at, status_by_domain, published_at, last_assignment_date, name_by_domain, rush_received, version, captation_done }
  ));

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
</script>

<table id="myTable">
	<thead>
    <tr> 
      {#each tableHeaders as header}
      <th on:click={() => (header === "has_high_priority" || header === "rush_received" || header === "captation_done" ) ? sortByNumber(header) : sortByString(header)}>
        <button on:click={() => ascendingOrder = !ascendingOrder}>
          {header
          .replace("title", "Projet")
          .replace("has_high_priority", "Priorité")
          .replace("categorie", "Catégorie")
          .replace("language", "Langue")
          .replace("created_at", "Créé le")
          .replace("status_by_domain", "Étape")
          .replace("published_at", "Mise en ligne")
          .replace("last_assignment_date", "Attribué le")
          .replace("name_by_domain", "Personne")
          .replace("rush_received", "Rushes récupérés")
          .replace("version", "Version")
          .replace("captation_done", "Captation réalisée")}
          <span class="order-icon">
            <Icon color="var(--grey)" width="15" height="15">
              <SortArrowIcon />
            </Icon>
          </span>		
        </button>	
      </th>
      {/each}
    </tr>
  </thead>
  <tbody>
	  <TableRow {selectedRowElements}/>
	</tbody>
</table>

<style>
  tr {
    white-space: nowrap;
  }
  th {
    padding: var(--spacing-3);
    text-align: left;
  }
  span {
    display: inline-block;
    vertical-align: middle;
    margin-top: var(--spacing-1);
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
    color: inherit;
    font: inherit;
    line-height: normal;
    -webkit-font-smoothing: inherit;
    -moz-osx-font-smoothing: inherit;
    -webkit-appearance: none;
  }
</style>